# 导入ecommerce包里整个shipping模块
from ecommerce import shipping
shipping.calc_shipping()
shipping.calc_walk()

# 导入ecommerce包里sales模块里的方法
from ecommerce.sales import calc_sales
calc_sales()

# 导入ecommerce包里整个buy模块
import ecommerce.buy

ecommerce.buy.calc_buy()
ecommerce.buy.calc_walk()
