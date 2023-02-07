<div align="center">
    <h1>Random Memes Project</h1>
    <h2>Web que muestra random memes scrapeados cada 30 segundos.</h2>
</div>

<details>
  <summary>Sumario</summary>
  <ol>
    <li>
      <a href="#desplegar-el-proyecto">Desplegar el proyecto</a>
    </li>
    <li>
      <a href="#tecnologías-usadas">Tecnologías usadas</a>
    </li>
    <li>
        <a href="#redes-sociales">Redes sociales</a>
    </li>
  </ol>
</details>

## Desplegar el proyecto

```bash
# Para inicializar la base de datos de Airflow
docker-compose up airflow-init
# Para inicializar los servicios de Airflow y el Frontend
docker-compose up
```

Para acceder a Airflow: http://localhost:8080/ (Usuario: airflow, Contraseña airflow)
Para acceder al frontend: http://localhost:3000 

## Tecnologías usadas

Para obtener memes randoms, usamos *Web Scraping*, utilizando [beautifulsoup](https://pypi.org/project/beautifulsoup4/) para extraer el contenido html de la página de memes -> https://www.generatormix.com/random-memes.

La página web está desarrollada con el framework [NextJs](https://nextjs.org/docs/deployment) y utilizando TypeScript.

## Redes Sociales

- [Linkedin](https://www.linkedin.com/in/enrique-ferrer-agius-05844a217/)

