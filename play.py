def quote(text): 
  return '"%s"' % text

def pack(*commands): 
  return ' '.join(commands)

def say(something, voice):
  if ':' in something:
    [voice, something] = (
      quote(part.strip())
      for part in something.split(':')
    )
  
  return pack(
    'echo %s: %s;' % (
      voice.rjust(10,'.'),
      quote(something)
    ),
    'say %s'       % quote(something),
    '-v %s'        % voice
  )

def person(name):
  def inner(something):
    return say(something, quote(name))
  return inner

def echo(times, text, voice, delay):
  from os import system

  return system(
    ';sleep 0.01;'.join(
      ['sleep %s' % delay]
      +
      list(
        map(
          lambda _: voice(text),
          range(times),
        )
      )
    )
  )

def spawn(text, voice, delay=0, times=10):
  from multiprocessing import Process
  p = Process(
    target=echo,
    args=(
      times,
      text,
      person(voice),
      delay
    )
  )
  p.daemon = True
  p.start()
  return p

def text():
  import fileinput
  return fileinput.input()

if __name__ == "__main__":
    import random

    for (time, line) in enumerate(text()):
      wait = time * 1.8
      spawn(
        line,
        random.choice([
          'yelda',
          'cem',
          'cem',
          'yelda',
          'zuzana'
        ]),
        wait,
        1
      );
    # spawn('halalûyāh' * 100, 'cello', 0.3, 10);
    # spawn('halalûyāh' * 100, 'good news', 0.3, 10);
    # spawn('yabadadabada', 'cem', 0, 10);
    # spawn('yabadadaybad', 'good news', 0, 10);

    try:
      while True:
        pass
    finally:
      print('.C^')
      exit()
