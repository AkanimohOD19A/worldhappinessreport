mkdir -p ~/.streamlit/

## whatever you do, do not accept this reccomendation - .stable_random_id - fucks this whole thing up

echo "\
[general]\n\
email = \"danielamahtoday@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml