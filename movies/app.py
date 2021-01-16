from flask import Flask, render_template, json, jsonify, request
import os
import requests

app = Flask(__name__)
json_info