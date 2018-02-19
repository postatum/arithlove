# arithlove
Arithmetic training tool.

## Install
```
pip install git+https://github.com/postatum/arithlove.git
```

## Run
```
arithlove path_to_conf.json
```

E.g. from `arithlove` project folder run:
```
arithlove example/conf.json
```

Type the answer (or don't) and press Enter to submit it.

Press `Ctrl+C` to exit.

## Config
Config JSON format is:
```
{
    "OPERATION_SIGN": [number1DigitsNum, number2DigitsNum]
}
```
Where `OPERATION_SIGN` is one of: `+, -, *, /`.

E.g. this config will:
* Generate `+` exercises containing 3 and 4-digit number;
* Do not generate `-` exercises;
* Use defaults for `*` and `/` operations (2 and 1-digit numbers).
```
{
    "+": [3, 4],
    "-": null
}
```
