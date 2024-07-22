import boto3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import boto3

# Configurar o driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
