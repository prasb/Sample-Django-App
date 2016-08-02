'''
Created on 25-Sep-2015

@author: prbalakr
'''
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    #val= "Hello World"
    
    return render(request, "index.html", {})
    #return HttpResponse(val)

def current_datetime(request):
    now = datetime.datetime.now()
    
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def drawtable(request):
    code = """<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
<title>Jenkins Results </title>
</head>

<body>

<body style="background-color:powderblue;">
<h1 style="text-align:center;" color ="black">Jenkins Result Mapper</h1>
<hr>

<p>Select a View</p>
<a href="http://www.w3schools.com">Click Here to Access Jenkins View</a>

<table>
  <tr>
    <th>Adaptation</th>
    <th>Total Test cases</th>
    <th>Passed</th>
    <th>Failed</th>
  </tr>
  <tr>
    <td>LTE</td>
    <td>23</td>
    <td>12</td>
    <td>11</td>
  </tr>
  <tr>
    <td>BSC</td>
    <td>23</td>
    <td>12</td>
    <td>11</td>
  </tr>
   <tr>
    <td>RNC</td>
    <td>23</td>
    <td>12</td>
    <td>11</td>
  </tr>
  <tr>
    <td>NTHLRFE</td>
    <td>23</td>
    <td>12</td>
    <td>11</td>
  </tr>
 <tr>
    <td>OMGW</td>
    <td>23</td>
    <td>12</td>
    <td>11</td>
  </tr>
   <tr>
    <td>openTAS</td>
    <td>23</td>
    <td>12</td>
    <td>11</td>
  </tr>
</table>
</body>
</html><html><head>
<style>
table, th, td {
    border: 1px solid black;
}
</style>
</head>
<body>

<table style="width:100%">
  <tr>
    <td>Test Case Name</td>
    <td>Site</td>        
    <td>Owner</td>
    <td>NE Names</td>
     <td>RNC</td>
    <td>OMGW</td>
    <td>NTHLRFE</td>
    <td>HSSFE</td>
    <td>CSCF</td>

  </tr>
  <tr>
    <td>AOM Upload</td>
    <td>Bangalore</td>        
    <td>Prasanna Balakrishnan</td>
   

  </tr>
  <tr>
    <td>AOM Activation</td>
    <td>Bangalore</td>        
    <td>Prasanna Balakrishnan</td>
    
  </tr>
</table>

</body>
</html>"""

    return HttpResponse(code)

