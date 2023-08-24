import json
import requests
print("Forever Tarafından Kodlanıp Yapılmştır!")

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='101m'  
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Bağlantı sağlandı. MySQL sunucusu sürümü:", db_Info)


        def kaydet(tc, adsoyad, dogumtarihi, ikametgah, tableName, connection):
       
            createTableQuery = f"CREATE TABLE IF NOT EXISTS {tableName} (TC VARCHAR(11) NOT NULL, AdSoyad VARCHAR(100) NOT NULL, DogumTarihi VARCHAR(10) NOT NULL, Ikametgah VARCHAR(255) NOT NULL)"

            with connection.cursor() as cursor:
                cursor.execute(createTableQuery)
                connection.commit()

           
                insertDataQuery = f"INSERT INTO {tableName} (TC, AdSoyad, DogumTarihi, Ikametgah) VALUES (%s, %s, %s, %s)"
                values = (tc, adsoyad, dogumtarihi, ikametgah)

                cursor.execute(insertDataQuery, values)
                connection.commit()

                print(f"Veri başarıyla kaydedildi: TC = {tc}")

     
        start_id = 4557  # Başlangıç ID'si
        end_id = 10000 # Bitiş ID'si

   
        sql1 = f"SELECT * FROM 101m WHERE id BETWEEN {start_id} AND {end_id}"

        with connection.cursor(dictionary=True) as cursor:  
            cursor.execute(sql1)
            result1 = cursor.fetchall()

            if cursor.rowcount > 0:
                for row1 in result1:
                    tc = row1['TC']

             
                    api_url = f".php?auth_key=adresapi&tc={tc}"  


                    response = requests.get(api_url)

                    if response.status_code == 200:
                        api_response = response.text

                        try:
                            api_data = json.loads(api_response)

                            if 'Data' in api_data:
                                api_data = api_data['Data']

                       
                                table_name = "veri3"
                                kaydet(api_data['TC'], api_data['AdSoyad'], api_data['DogumTarihi'], api_data['Ikametgah'], table_name, connection)
                            else:
                                print("API yanıtı geçerli bir veri içermiyor.")
                        except json.JSONDecodeError:
                            print("API yanıtı geçerli bir JSON verisi değil.")
                    else:
                        print("API'ye istek gönderirken hata oluştu veya yanıt alınamadı.")
            else:
                print("İlk veritabanında belirtilen ID aralığında kayıt bulunamadı.")

except Error as e:
    print("Veritabanına bağlanırken hata oluştu:", e)

finally:
    if connection.is_connected():
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.")
