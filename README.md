![](https://snapengage.com/wp-content/uploads/2018/07/chatbot-blog-banner-72618.png)
# Bot Army
This project is based on **Web Automation**. This is started with an idea to make a bot that can **attend online classes**. But now this has more than that, a **Bot Army** that will do everything for you.

### Steps to run
- Each **.py** file has a specific work to perform **(Instructions are provided at the start of each file)**
1. Fork this Repo
2. Clone that forked repo into your local system
3. Install `selenium` and `wedriver_manager` from **terminal**: (in **Windows**)
    1. `pip install selenium`
    2. `pip install webdriver-manager`
4. Now you can use any bot you want

### Problems you may face
- Problem 1: `selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element:{...}`

    - This is a race condition where the 'find element' is executing before it is present on the page. You just have to increase the no. of seconds so that the page will load properly.

    - `time.sleep(x)` -> This will suspend execution of code for **x seconds**

### Support
If you like this project, don't forget to give it a ⭐
