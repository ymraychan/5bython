# 5bython
A python port of HTML5b, which is an HTML5 port of BFDIA 5b

## Requirements
* pygame-ce 2.6.1
* scipy 1.16.2

## Build instructions

Install python using the offical python downloader: https://python.org.

Then, open Command Prompt (on windows) or Terminal (on Mac or Linux) and run:

```bash
pip install pygame-ce scipy # For windows
pip3 install pygame-ce scipy # For Mac / Linux
```

If you already have pygame installed, run

```bash
pip uninstall pygame # For windows
pip3 uninstall pygame # For Mac / Linux
```

However, some of your pygame games may stop working. Mine did when I upgraded. To fix that, replace

```python
pygame.display.set_caption(title=YOUR_TITLE) # Replace this
pygame.display.set_caption(YOUR_TITLE) # with this
```

Before emailing ymraychan+5bython@gmail.com, PLEASE, PLEASE try to fix it yourself. I really don't want spam.

## Statuses

* Borders: complete
* Blocks: partially complete (need to fix anchors)
* Entities: partially complete (have to fix a lot)
* Playing: not started
* Glitches: not started