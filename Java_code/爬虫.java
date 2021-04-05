import java.util.Scanner;
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

public class 爬虫 {
    public static void main(String[] args){
        html = urlopen("http://www.pythonscraping.com/pages/page3.html")
        bsObj = BeautifulSoup(html,'html.parser')
        images = bsObj.find_all("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
        for image in images:
        print(image["src"])
    }
}
