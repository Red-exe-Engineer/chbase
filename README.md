# Install
Just put it in `/usr/bin/` as `chbase`, don't forget to run `chmod +x /path/to/chbase`.

# Usage
By default it converts from base 10 to 16, you can change this by using the following arguments:
- -f --from
- -t --to

You can also change the padding (or remove it) with `-p` or `--pad`, padding must be 0-1 characters long.

# Examples:
```
$ chbase 15 16 100
 F
10
64
```

```
$ chbase -f32 -t16 C1VVE
C0FFEE
```

```
$ chbase -f16 -t10 10 3A 7D38 2 C0FFEE FFE4A1
      16
      58
   32056
       2
12648430
16770209
```

```
$ chbase --from hex --to oct --pad "." 10 2048
..14
4948
```

Tip: `-p`/`--pad` can be `""` for no padding.

The `convert_number` function used some of [Alex Martelli](https://stackoverflow.com/a/2267446/19348326)'s code, thanks!
