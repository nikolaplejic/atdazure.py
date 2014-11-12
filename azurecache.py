import redis
import azurecfg

r = redis.StrictRedis(host=azurecfg.redis['host'],
                      password=azurecfg.redis['auth'])
