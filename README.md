# readme-classifier
this is a classifier that is used to determine whether a github readme file is "good" or "bad"

this idea behind this project was to change the [static classifier](https://github.com/oubaydos/DevOpsify/tree/main/devopsify-backend/src/main/java/com/winchesters/devopsify/service/technologies/github/readme) found in [DevOpsify](https://github.com/oubaydos/DevOpsify)

### score 
for now the score for this model is *94%*, but i think there could be a problem of overfitting, i will do more tests 

### example
when given this Readme
```python
test_readme = """
#this readme
"""
```
it gives 
```python
print(predict(test_readme))
# False
```
so apperently this is a bad readme 😂
