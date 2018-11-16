# PyMonitor

## A simple tool to notify you about errors via system notifications and Telegram.


### Usage

Library provides very simple 3 use cases,

1. Apllying the notification on the complete script, i.e any error on `__main__` will be caught    and reported to the user.

    `form error_notify import total_override`

2. Getting error notifications from a single function

    `from error_notify.decorators import override_function`

    ```
    @override_function
    def test_funct():
    	pass
    ```

3. Getting error notification from a class

   `from error_notify.decorators import override_class`

   ```
   @override_class()
   class DemoClass(object):
       def func_1():
           pass
       def funct_2():
           pass
    ```

    `override_class` takes 2 optional parameter, `include` and `exclude`. These are a list with names of method to be excluded or included. By default all the methods are included.


### Example
* Clone the repo
* `cd error_notify`
* `cd examples`
* `python example.py [option]`
    
    Options - `total`, `partial`, `class`

