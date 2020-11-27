![](https://snapengage.com/wp-content/uploads/2018/07/chatbot-blog-banner-72618.png)
# Bot Army
This project is based on **Web Automation**. This is started with an idea to make a bot that can **attend online classes**. But now this has more than that, a **Bot Army** that will do everything for you.

## Community
**[Code of Conduct](https://github.com/inaxia/attendance_using_face_recognition/blob/master/CODE_OF_CONDUCT.md)**<br>
**[Contributing to Inaxia](https://github.com/inaxia/attendance_using_face_recognition/blob/master/CONTRIBUTING.md)**

## Steps to run
- Each **.py** file has a specific work to perform **(Instructions are provided at the start of each file)**
1. Fork this Repo
2. Clone that forked repo into your local system
3. Install `selenium` and `wedriver_manager` from **terminal**: (in **Windows**)
    1. `pip install selenium`
    2. `pip install webdriver-manager`
4. Now you can use any bot you want

## Problems you may face
- Problem 1: `selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element:{...}`

    - This is a race condition where the 'find element' is executing before it is present on the page. You just have to increase the no. of seconds so that the page will load properly.

    - `time.sleep(x)` -> This will suspend execution of code for **x seconds**

## Reference link
Image from Google: https://camo.githubusercontent.com/5ef0bf665905bb7b3040547ea95eeb75a047427b5246e5e99ea7b2aa533af89e/68747470733a2f2f736e6170656e676167652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031382f30372f63686174626f742d626c6f672d62616e6e65722d37323631382e706e67

## Support
If you like this project, don't forget to give it a ⭐
