# We will import weight_converter_module.py as a module and work with it here.

# METHOD 1 - import entire module
import weight_converter_module
print(weight_converter_module.kgs_to_lbs(70))

# METHOD 2 - import specific method
from weight_converter_module import lbs_to_kgs
print(lbs_to_kgs(31.5))

from utils import calculate_shipping
print(calculate_shipping.calc_shipping())
