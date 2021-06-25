
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About The Project
This project consistis in a web scraper that collects daily news about the COVID19 pandemic from the BBC Brazil website ([https://www.bbc.com/portuguese](https://www.bbc.com/portuguese)), store them in a Postgres database and make useful information available through an API.

### Built With
* Python
* Postgresql
* Docker

## Project Architecture
![plot](diagram.png)

## Getting Started

### Prerequisites
* Docker
```sh
sudo apt get docker
```
* Docker-compose
```sh
sudo apt get docker-compose
```
### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/brianamaral/covid-news.git
  ```
2. Change de environment variables in the docker-compose.yml
  ```docker
  - POSTGRES_USER=
  - POSTGRES_PASSWORD=
  - POSTGRES_DB=
  ```
3. Change the variables in the webscraper/first_page.py and api/main.py
  ```python
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  POSTGRES_ADDRES = '' 
  POSTGRES_DATABASE = '' 
  ```
## Usage
If you changed the variables above correctly, then you are good to go, just go to the docker folder and then run:
```sh
docker-compose up
```
### API Endpoints
* /all_articles: return all articles on the dabatase
* /last_article: return the last articles on the database by the date


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Brian Bomfim Amaral - [Linkedin](https://www.linkedin.com/in/brian-amaral-29013a200/) - brian.amaralt@gmail.com

Project Link: [https://github.com/brianamaral/covid-news](https://github.com/brianamaral/covid-news)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Schedule](https://schedule.readthedocs.io/en/stable/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Sqlalchemy](https://www.sqlalchemy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Docker](https://www.docker.com/)
* [Postgresql](https://www.postgresql.org/)



