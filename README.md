# DRF Edu Projects

Django Rest Framework ile Edu Api projesi.


## Kurulum

Not: Sol taraftaki veriler Mac kurulumu için sağ taraftaki veriler Windows kurulumu içindir.

Projeyi Kurma  

```bash
 git clone https://github.com/tarikberkay/edu.git
```

Sanal Ortam Oluşturma
```bash
  python3 -m venv venv || python -m venv venv
```

Sanal Ortamı Aktif Etme
```bash
  source venv/bin/activate  ||  venv\Scripts\activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -r requirements.txt
```


Projeyi Çalıştırma
```bash
  python3 manage.py runserver || python manage.py runserver
```

  
## API Kullanımı

#### Öğeyi getir

```http
  http://127.0.0.1:8000/
```
Router Endpointleri getirir.


#### Tüm EndPointleri getirir

```http
  http://127.0.0.1:8000/api/
```



#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/courses/
```


Kursları getirir.




#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/classrooms/
```

Sınıfları getirir.



#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/students/
```
Öğrencileri getirir.



#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/teachers/
```
Öğretmenleri getirir.







#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/docs/
```

Swagger ile API'nin belgelenmesi sağlanmıştır.



#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/schema/
```

API belgesi indirilebilir.


