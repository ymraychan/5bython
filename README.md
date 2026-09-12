# 5bython
A python port of HTML5b, which is an HTML5 port of BFDIA 5b

## Requirements
* pygame-ce 2.6.1
* scipy 1.16.2
* mypyc 2.1.0 (optional)
* pyinstaller 6.19.0 (optional)

## Run instructions
Find the latest exe/app release and run it. If you want an older version find the older version.

## Build instructions
Install python using the offical python downloader: https://python.org.
Then, clone this repository. Do
```bash
pip install . --user --break-system-packages
```
DISCLAIMER: Using `--break-system-packages` may, well, break your system packages if you use different versions of the dependencies.

Then, run
```bash
cd src/ && python 5b.py
```
If that throws an error complaining `python` is not a command, run
```bash
python3 5b.py
```

## Statuses

* Borders: complete
* Blocks: partially complete (need to fix anchors)
* Entities: partially complete (have to fix a lot)
* Playing: not started
* Glitches: not started


## Credits

* **[coppersalts](https://github.com/coppersalts)** — For creating **HTML5b**, from which design and functional assets were used.
* **Cary and Michael Huang** — For creating and open-sourcing **Battle for Dream Island**.

## License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. 

Because it incorporates code or assets from [HTML5b](https://github.com/coppersalts/HTML5b), which is distributed under the GPLv3, this entire project is bound by the same copyleft terms. 

See the [LICENSE](LICENSE) file for the full text.