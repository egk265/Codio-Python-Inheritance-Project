class Parent1:
  def identify(self):
    return "This method is called from Parent1"
    
class Parent2:
  def identify(self):
    return "This method is called from Parent2"
    
# declare child class here
class Child(Parent1, Parent2):
  def identify(self):
    return "This method is called from Child"
  def identify2(self):
    super().identify()
    
child_object = Child()
print(child_object.identify())
print(child_object.identify2())

