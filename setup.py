import setuptools
  
setuptools.setup(
    #Here is the module name.
    name="weather",
 
    #version of the module
    version="0.0.1",
 
    #Name of Author
    author="Santhosh R",
 
    #your Email address
    author_email="santhoshgowda.ec@gmail.com",
 
    #Small Description about module
    description="Web scrapping for weather.com",

 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Pushkar-Singh-14/",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)