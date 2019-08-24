# Snaaaaaaaaaake Game!!

어쩌다 난 이런 걸 만들게 되었을까...

I don't understand why I'm making this shit.

![solid snake](./statics/snake.jpeg)

```sh
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
./run.py <type> <renderable> <count>
```

#### type

0: 직접 플레이할 수 있습니다 (Manual play)

1: 랜덤으로 움직입니다 (Random)

2: 무조건 직진맨입니다 (Straight)

3: 길찾아 움직입니다 (Simple BFS Pathfinder)

#### renderable

`type`이 1 이상일 경우 적용할 수 있습니다.

1: 과정을 화면에 표시해줍니다.

0: 과정을 화면에 표시하지 않고 결과만 표시합니다.

#### count

`renderable`이 0일때 적용할 수 있습니다.

`count`번 만큼 시행합니다.
