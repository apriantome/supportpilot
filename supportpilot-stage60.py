# === Stage 60: Add saved views for frequently used filters ===
# Project: SupportPilot
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}
    
    @staticmethod
    def load_from_json(filepath):
        import json
        with open(filepath, 'r') as f:
            data = json.load(f)
        views = []
        for item in data.get('views', []):
            view = SavedView(item['name'], item.get('filters', {}))
            views.append(view)
        return views
    
    @staticmethod
    def save_to_json(filepath, views=None):
        import json
        if views is None:
            views = []
        data = {'views': [{'name': v.name, 'filters': v.filters} for v in views]}
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def apply(self, query):
        for key, value in self.filters.items():
            if hasattr(query, key) and getattr(query, key) != value:
                return False
        return True
    
    def __repr__(self):
        return f"SavedView(name={self.name!r}, filters={self.filters})"
