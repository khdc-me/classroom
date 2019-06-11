Pg 54 | Table 3-5 | PHP's [magic contants](https://www.php.net/manual/en/language.constants.predefined.php)

```php
__LINE__ // Current line # of file.


__FILE__ // Full path & filename of file.


__DIR__ // Directory of the file.


__FUNCTION__ // The function name.


__CLASS__ // The class name.


__METHOD__ // The class method name.


__NAMESPACE__ // Name of current namespace.
```
----

[htmlentities](https://www.php.net/manual/en/function.htmlentities.php) to sanitize user or 3rd-party data when being processed for output.
----
Pg 60 | Table 3-6 | PHP's [superglobal variables](https://www.php.net/manual/en/language.variables.superglobals.php)

```php
$GLOBALS // All variables defined in script's global scope. Names are keys of the array.

$_SERVER // Info on headers, paths, locations of scripts. Entries created by web server (no guarantee every server will provide any of these)

$_GET // Variables passed via HTTP GET method.

$_POST // Variables passed via HTTP POST method.
... Many more that can be found following link above.
```
All superglobals (except $GLOBALS) start w/ an underscore. Avoid starting variable names w/ an underscore.