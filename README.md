## Fetch Youtube Videos List 

A Django Application to make an API to fetch latest Youtube videos for "football" query sorted in reverse chronological order according to their publishing date-time for a given tag/search query in a response.


## Functionalities
- Fetch Youtube Videos and save information to SQL database 
- View fetched videos in a paginated response

## Installation
Clone this git repository:
```
git clone https://github.com/kirtish16/yt_API_Fetch.git
```
Go to the project folder:
```
cd ytAPI
```
Install the requirements:
```
pip install -r requirements.txt
```

Run the migrations:
```
python manage.py migrate
```
Start the server:
```
python manage.py runserver
```
This will start the webserver on [localhost](http://127.0.0.1:8000/).

## Documentation
The API endpoints are:

| Endpoint   | Description |
|------------|-----------|
| /get/ | fetch all videos and save to Database|
| / | get all videos saved in Database in a paginated response |


## Screenshots 

+ Fetching videos 

  ![Success](/Screenshots/success.png)
 
+ Paginated response of saved videos 

  ![Response](/Screenshots/response.jpg)
 



## License
[MIT](https://choosealicense.com/licenses/mit/)
