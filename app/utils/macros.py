from datetime import datetime
from dateutil.relativedelta import relativedelta
import itertools

def resolve_macros(params: dict) -> dict:
    """
    Replaces known string macros in the dictionary values with actual dates.
    Supported macros: {{today}}, {{yesterday}}, {{this_month_start}}, 
    {{this_month_end}}, {{last_month_start}}, {{last_month_end}}
    """
    if not isinstance(params, dict):
        return params

    resolved = {}
    now = datetime.now()
    
    macros = {
        "{{today}}": now.strftime("%Y-%m-%d"),
        "{{yesterday}}": (now - relativedelta(days=1)).strftime("%Y-%m-%d"),
        "{{this_month_start}}": now.replace(day=1).strftime("%Y-%m-%d"),
        "{{this_month_end}}": (now + relativedelta(months=1, day=1) - relativedelta(days=1)).strftime("%Y-%m-%d"),
        "{{last_month_start}}": (now - relativedelta(months=1)).replace(day=1).strftime("%Y-%m-%d"),
        "{{last_month_end}}": (now.replace(day=1) - relativedelta(days=1)).strftime("%Y-%m-%d"),
    }
    
    for k, v in params.items():
        if isinstance(v, str) and v in macros:
            resolved[k] = macros[v]
        elif isinstance(v, str):
            # Also support macros embedded in strings (e.g. "date_{{today}}")
            new_v = v
            for m_key, m_val in macros.items():
                if m_key in new_v:
                    new_v = new_v.replace(m_key, m_val)
            resolved[k] = new_v
        else:
            resolved[k] = v
            
    return resolved

def explode_params(params: dict) -> list[dict]:
    """
    Takes a dictionary where some values might be lists, and returns a 
    list of dictionaries representing the Cartesian product of those values.
    
    Example:
    {"a": [1, 2], "b": 3} -> [{"a": 1, "b": 3}, {"a": 2, "b": 3}]
    """
    if not params:
        return [{}]
        
    keys = list(params.keys())
    # Ensure all values are wrapped in a list for itertools.product
    val_lists = [v if isinstance(v, list) else [v] for v in params.values()]
    
    combinations = []
    for combo in itertools.product(*val_lists):
        combinations.append(dict(zip(keys, combo)))
        
    return combinations
