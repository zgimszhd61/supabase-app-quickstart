from supabase import create_client, Client

url: str = ""
key: str = ""
supabase: Client = create_client(url, key)

data = {"task": "完成Supabase项目", "done": False}
inserted_data = supabase.table("todos").insert(data).execute()
