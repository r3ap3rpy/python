import redis
import ssl

##stunnel.conf
#foreground = yes
#cert = private.pem
#[redis]
#accept = 0.0.0.0:6666
#connect = 127.0.0.1:6379

##generate rsa
#openssl genrsa -out key.pem 4096
#openssl req -new -x509 -key key.pem -out cert.pem -days 1826 -batch
#cat key.pem cert.pem > private.pem
#chmod 640 key.pem cert.pem private.pem

pool = redis.ConnectionPool(
connection_class=redis.SSLConnection,
host='172.17.157.69',
port=6666,
ssl_ca_certs='private.pem',
ssl_cert_reqs=ssl.CERT_REQUIRED)
r = redis.StrictRedis(connection_pool=pool)

print(r.ping())