from contextlib import nullcontext
from encodings.base64_codec import base64_encode
from random import randbytes, random
import os
from secrets import *
import base64
import json
import requests
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

def read_file(filename):
    f= open(filename);
    for line in f.readlines():
        print(line);


def join_string(a,b):
    if not (isinstance(a,str) and isinstance(b,str)):
        print("a is a string ? : " + str(isinstance(a,str) ))
        print("b is a string ? : " + str(isinstance(b,str) ))

        return None;

    return a+b;


def num_power(a,b):
    if not(isinstance(a,int) and isinstance(b,int)):
        print("a and b should be int ? : " + str(isinstance(a,int) and isinstance(b,int)));
        return None;
    return a**b;

def rangin_printing(num):
    for i in range(num):
        print("hello " ,str(i));
    return;

def create_base64(n):
    val = random_bytes = os.urandom(n);
    #print(val)
    r = val;
    r = base64_encode(val)
    #print(r)
    return r;


def generate_base64_string(length=24):
    # Base64-encoded string length is approximately 4/3 of the original byte length.
    # To get 24 characters, we need (24 * 3 / 4) = 18 bytes.
    byte_length = (length * 3) // 4

    # Generate random bytes
    random_bytes = os.urandom(byte_length)

    # Encode bytes to base64 and decode to string
    random_base64_string = base64.urlsafe_b64encode(random_bytes).decode('utf-8')

    # Trim the string to the desired length
    #return base64_string[:length]
    return random_base64_string;


def get_vegmeals():
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Vegetarian"
    response = requests.get(url,verify=False)
    return response.json().get('meals',[])
    #print(response.json())

def get_ingredients(id):
    url = "https://www.themealdb.com/api/json/v1/1/lookup.php?id=" + id
    print(url)
    response = requests.get(url,verify=False)
    print(response)
    #return response.json().get('meals',[])
    #print(response.json())

