# 데이터 크롤링

* 모델링을 위한 데이터 이미지를 크롤링 하는 코드이다
* 크롤링은 크롬드라이버와 `selenium` 라이브러리를 이용해서 진행했다.

```python
from selenium import webdriver

term_list1 = ['man', 'woman', 'child', 'boy', 'girl', '남자' ,'얼굴']
term_list2 = ['mask face', 'face mask', 'kf94 mask face', 'coronavirus mask', 'face mask kf80', 
              'surgery mask', 'construction mask', '마스크']
term_list3 = ['room', '복도', '방']

# term_list = {"face" : term_list1, "mask" : term_list2}
# term_list = {"background" : term_list3}

for name in term_list:
    idx  = 1

    for term in term_list[name]:
        url = "https://www.google.co.in/search?q=" + term + "&tbm=isch"
        browser = webdriver.Chrome("lib/chromedriver.exe")
        browser.get(url)
    
    #     for i in range(100):
    #         browser.execute_script('window.scrollBy(0,10000)')
    
        for el in browser.find_elements_by_class_name("rg_i"):
            el.screenshot("./img/raw image/" + name + "/" + str(idx) + ".png")
            idx += 1
        browser.close()
```



* 위의 코드는 아래의 블로그의 코드를 참고하여 작성하였다.
  * <https://brunch.co.kr/@needleworm/52>