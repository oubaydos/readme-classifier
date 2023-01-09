import os
from time import sleep

import github.Repository
from github import Github

from config import api_key
from main import count

done_keywords = ["java", "scraper", "cli", "data", "ui", "front", "framework", "google", "facebook", "alpha", "stack",
                 "forum", "twitter", "python", "docker", "maven", "game", "android", "cpp", "github", "website",
                 "platform", "bot", "microservices", "integration", "json", "system", "ios", "script", "fullstack",
                 "service", "test", "api", "web", "modern", "3d", "algorithm", "aws", "devops", "review"]


def scrape(stars_query="stars:>10000", forks_query="forks:>50", order="desc", res_folder="res", max_scraped=3000,
           keywords=None, scraped_results_counter=count()):
    if keywords is None:
        keywords = done_keywords
    g = Github(api_key)
    # repos= [g.get_repo("oubaydos/Devopsify")]
    counter = 0
    for j in range(len(keywords)):
        repos = g.search_repositories(query=keywords[j] + " " + stars_query + " " + forks_query, sort="stars",
                                      order=order)
        print("--------------------")
        print("--------------------")
        print(j)
        print("--------------------")
        print("--------------------")
        temp_counter = 0
        for i in repos:
            if temp_counter > (max_scraped - scraped_results_counter) / len(keywords):
                break
            temp_counter += 1
            try:
                counter += 1
                print(i.name, i.stargazers_count)
                if not os.path.exists(res_folder + "/" + keywords[j]):
                    os.makedirs(res_folder + "/" + keywords[j])
                print(i.get_readme().decoded_content,
                      file=open(res_folder + "/" + keywords[j] + "/" + str(counter) + '.md', 'w'))
            except github.UnknownObjectException as e:
                print("github exception")
                print(e)
            except Exception as e:
                print(e)
                sleep(5)
    print(counter)


def scrape_bad_readmes():
    scrape(stars_query="stars:<3", order="asc", res_folder="bad-res", forks_query="forks:<2",
           keywords=["easy", "hello", "azure", "desktop", "movile", "stream", 'tp', 'personal', "homework"],
           scraped_results_counter=count("bad-res"))


scrape_bad_readmes()
