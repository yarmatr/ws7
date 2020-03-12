#wml_python_function
def score(payload):
    """AI function example.
    
    Example:
      {
        "fields": ["Gender", "Status", "Children", "Age", "Customer_Status"],
        "values": [
          ["Male", "M", 2, 48, "Inactive"],
          ["Female", "S", 0, 23, "Inactive"]
        ]
      }
    """
    fields = payload['fields'] + ['Prediction', 'Probability']
    values = [record + [int(record[0] == 'Male'), 0.9] for record in payload['values']]
    return { 'input_data': [{ fields': fields, 'values': values }]}