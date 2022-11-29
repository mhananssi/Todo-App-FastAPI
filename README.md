<h1> FastAPI for Todo App </h1>

<h2> Project Setup </h2>

<p> Running app through <a href="https://docs.docker.com/compose/">docker-compose</a> <pre> <code> docker-compose up </code> </pre> <p>

<p> To tear down the setup <pre> <code> docker-compose down </code> </pre> <p>

<h2> Accessing Application </h2>

<table>
  <tr>
    <td>todo api</td>
    <td><a href="http://localhost:8000">http://localhost:8000</a></td>
  </tr>
  <tr>
    <td>swagger documentation</td>
    <td><a href="http://localhost:8000/docs">http://localhost:8000/docs</a></td>
  </tr>
    <tr>
    <td>redoc documentation</td>
    <td><a href="http://localhost:8000/redoc">http://localhost:8000/redoc</a></td>
  </tr>
  <tr>
    <td>postgres database</td>
    <td>postgres-container-ip:5432</td>
  </tr>
</table>

<p><small> You can access the database using some database client. Use <a href="https://docs.docker.com/engine/reference/commandline/inspect/">docker inspect</a> to find the postgres-container-ip </small> </p>

<h2> Installing package in a running container using <a href="https://docs.docker.com/engine/reference/commandline/exec/">docker exec</a></h2>

<pre> <code> docker exec container pip install package </code> </pre>