require 'watir'
require 'colorize'
require 'time'

def estimated_time(start_time, progress)
  elapsed_time = Time.now - start_time
  total_time = elapsed_time / progress
  remaining_time = total_time - elapsed_time

  hours = (remaining_time / 3600).floor
  minutes = ((remaining_time % 3600) / 60).floor
  seconds = (remaining_time % 60).floor

  format('%02d:%02d:%02d', hours, minutes, seconds)
end

def print_progress(progress, start_time)
  total_width = 100
  filled = (total_width * progress).round
  remaining = total_width - filled

  print "\r[products_az_html]["
  print "#".colorize(:green) * filled
  print " ".colorize(:white) * remaining
  print "] #{(progress * 100).round(2)}% ETA: #{estimated_time(start_time, progress)}"
end

custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
options = {
  args: [
    "--user-agent=\"#{custom_user_agent}\"",
    '--disable-gpu',
    '--disable-dev-shm-usage',
    '--disable-setuid-sandbox',
    '--no-first-run',
    '--no-sandbox',
    '--no-zygote',
    '--single-process',
    '--blink-settings=imagesEnabled=false',
    '--blink-settings=CSSImagesEnabled=false',
    '--headless'
  ]
}

browser = Watir::Browser.new :chrome, options: options

Dir.mkdir('products_az_html') unless Dir.exist?('products_az_html')

urls = File.readlines('products_az.txt', chomp: true)

file_counter = 1
total_urls = urls.size

start_time = Time.now

MAX_RETRIES = 100
RETRY_SLEEP = 5

begin
  urls.each_with_index do |url, index|
    if File.exist?("products_az_html/#{file_counter}.html")
      puts "File #{file_counter}.html already exists. Skipping..."
      file_counter += 1
      next
    end

    retries = 0
    success = false
    
    while retries < MAX_RETRIES && !success
      begin
        browser.goto(url)
        sleep(2)

        source_code = browser.html
    
        File.open("products_az_html/#{file_counter}.html", 'w') do |file|
          file.write(source_code)
        end
    
        success = true
    
      rescue Net::ReadTimeout
        retries += 1
        sleep(RETRY_SLEEP) if retries < MAX_RETRIES
        puts "\nTimeout error accessing #{url}. Retrying (attempt #{retries}/#{MAX_RETRIES})..." if retries < MAX_RETRIES
      end
    end

    unless success
      puts "\nFailed to access #{url} after #{MAX_RETRIES} attempts. Skipping..."
      next
    end
    
    file_counter += 1
    progress = (index + 1).to_f / total_urls
    print_progress(progress, start_time)
  end

  puts "\nAll pages have been saved.".colorize(:green)
rescue StandardError => e
  puts "\nAn unexpected error occurred: #{e.message}".colorize(:red)
ensure
  browser.close if browser
end