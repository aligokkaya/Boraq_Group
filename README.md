# Boraq_Group

Project  
Flask + BluePrint +SQLAlchemy+ MySql + RestApi + Docker + Apache Deploy  

This project news site  


Setup:  
  
By pulling the codes from the repo, the order is first brought to the Flask dockerfile.  
  
```
docker build ./ --tag boraq_group  
docker run --restart always -d --network=host --name boraqdeploy boraq_group  
```

The site consists of 3 stages.  

1-Current news was taken from a web service  
2-Posting news from admin control  
3-Admin login page  



  
1-Current news was taken from a web service :  
Inside the Flask folder, there is an apache config file without SSL ready to be deployed. Database Mysql is used. Data is retrieved as it is entered on each page.
  
![alt text](https://github.com/aligokkaya/Boraq_Group/blob/main/readme_image/1.png)


2:Posting news from admin control  
In this section, it lists the news that the admin has shared.
![alt text](https://github.com/aligokkaya/Boraq_Group/blob/main/readme_image/2.png)
  
Details of news published by admin  
![alt text](https://github.com/aligokkaya/Boraq_Group/blob/main/readme_image/3.png)

3-Admin login page:  
  
![alt text](https://github.com/aligokkaya/Boraq_Group/blob/main/readme_image/4.png)
  
```
Admin Login :  
    boraq123@gmail.com  
password:  
    boraq123  

```

interface where admin will add news:
  
![alt text](https://github.com/aligokkaya/Boraq_Group/blob/main/readme_image/51.png)

  
Interface prepared for the admin to see the news they have add, delete, update these news in the database.  

   
![alt text](https://github.com/aligokkaya/Boraq_Group/blob/main/readme_image/6.png)




RESTAPI :  
  
1-  
Desired endpoint to create a new user  

```
URL POST:
http://127.0.0.1/challange/register/  

```
and  
```
data ={

"mail":"test@gmail.com",
"name_surname":"test",
"password":"test"
}
```  

  

2-  
Pulls the latest news shared by the admin  


```
News GET:  
r=requests.get('http://127.0.0.1/v1/boraq/news')   
```









  



