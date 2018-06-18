### Text-to-speech Acapella Tool

Demo: 
https://www.youtube.com/watch?v=u_zhUZiBnFU

### How to use

    seq 5 | xargs echo zuzana:$1 | python3 play.py
    seq 5 | xargs echo cello: $1 | python3 play.py
    seq 5 | xargs echo yelda: $1 | python3 play.py
    seq 5 | xargs echo cem:   $1 | python3 play.py
    cat   |                        python3 play.py
