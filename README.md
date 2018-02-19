# arithlove
Arithmetic training tool

## Install
```
git clone https://github.com/postatum/arithlove.git
cd arithlove
pip install .
```

## Run
```
arithlove path_to_conf.json
```

E.g. from `arithlove` project folder run:
```
arithlove example/conf.json
```

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
