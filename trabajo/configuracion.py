#cadena_base_datos = 'sqlite:///futredx.db' 
#docker run --name my-postgres-db \
#-e POSTGRES_USER=root \
#-e POSTGRES_PASSWORD=1234 \
#-e POSTGRES_DB=final \
#-p 5432:5432 \
#-d postgres

#sudo docker stop my-postgres-db

#sudo docker rm my-postgres-db

cadena_base_datos = "postgresql://root:1234@localhost:5432/final"
