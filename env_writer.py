import sys

with open('.env', 'w') as f:
    username = input("Enter your bot username:\n")
    f.write('ENV_PLACE_USERNAME=\'["'+username+'"]\n')
    password = input("Enter your bot password\n")
    f.write('ENV_PLACE_PASSWORD=\'["'+password+'"]\n')
    client = input("Enter your client ID\n")
    f.write('ENV_PLACE_APP_CLIENT_ID=\'["'+client+'"]\n')
    secret = input("Enter your secret key\n")
    f.write('ENV_PLACE_SECRET_KEY=\'["'+secret+'"]\n')
    f.write('ENV_DRAW_X_START="299"\nENV_DRAW_Y_START="449"\nENV_R_START=\'["0", "5", "10", "15", "20","25","30","35","40","45"]\'\nENV_C_START=\'["0", "4", "8", "12", "16" ,"20", "24", "28", "32", "36"]\'\n')
    print(f"Adding your bot {username} to the .env file\n")
