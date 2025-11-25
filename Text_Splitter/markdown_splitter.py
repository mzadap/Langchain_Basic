from langchain.text_splitter import MarkdownTextSplitter


text = """
# TESTNG Command Line Guide
## 1. Run Test using command Line
To run all tests:
```
mvn test
```
## 2. Run a Single Test Method
To run a specific test method:
```
mvn test -Dtest=ClassName#testMethodName
```
## 3.Run Multiple Groups
To run tests from multiple groups:
```
mvn test -Dgroups="group1,group2"
```

## 4.Run a Single Group
To run tests from a single group:
```
mvn test -Dgroups="groupName"
```

## 5. Run All Test Methods That Match a Pattern from a Class
To run tests that match a specific pattern:
```
mvn test -Dtest=ClassName*Pattern
```
## 6. Run Single Test Using testnames Property in testng.xml
Add the ```selectedTests``` in propertries tag
```
<selectedTests>selectedTests</selectedTests>
```
Run it with
```
mvn test -DselectedTest=Regression-test
```

## 7. Run Multiple TestNG XML Files
First, declare `suiteXmlFile` with a valid variable name i.e `suites` in the properties section
To run multiple testng.xml files:
```
mvn test -Dsuite=Regression.xml,Sanity.xml,Smoke.xml
```

## 8.Create Profile and Run Profiles
Define profiles in pom.xml and run with:
```
mvn test -Psmoke    //smoke is id that you will give in <id> tag
```

"""


splitter = MarkdownTextSplitter(
    chunk_size=150,
    chunk_overlap=0
)

result = splitter.split_text(text)
print(len(result))
print(result[0])