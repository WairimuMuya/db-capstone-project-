{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2fd2c76b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: mysql-connector-python in c:\\users\\user\\anaconda3\\lib\\site-packages (8.0.32)\n",
      "Requirement already satisfied: protobuf<=3.20.3,>=3.11.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from mysql-connector-python) (3.19.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install mysql-connector-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "895c7906",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector as connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b9b317d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "connection = connector.connect(user = \"root\", password = \"rose\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e5fec5d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "connection = connector.connect(user = \"root\", password = \"rose\", db = \"littlelemondm\")\n",
    "cursor=connection.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "34ac4629",
   "metadata": {},
   "outputs": [],
   "source": [
    "show_tables_query = \"SHOW tables\" \n",
    "results = cursor.execute(show_tables_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a7408e72",
   "metadata": {},
   "outputs": [],
   "source": [
    "results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a0b67c45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " menu\n",
      "bookings\n",
      "customersdetails\n",
      "menuitems\n",
      "orderdeliverystatus\n",
      "orders\n",
      "staffdetails\n"
     ]
    }
   ],
   "source": [
    "tables = cursor.fetchall()\n",
    "for table in tables:\n",
    "    print(table[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "520ac3ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "customer_join_query = '''\n",
    "        SELECT\n",
    "            c.CustomerID AS CustomerID\n",
    "            c.Name AS FullName,\n",
    "            c.Email AS Email,\n",
    "            c.ContactNumber AS ContactNumber,\n",
    "            o.TotalCost AS Cost\n",
    "        FROM Customersdetails c\n",
    "        JOIN orders o\n",
    "            USING (CustomerID)\n",
    "        WHERE o.TotalCost > 60\n",
    "        ORDER BY o.TotalCost DESC;\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "67b6a941",
   "metadata": {},
   "outputs": [
    {
     "ename": "ProgrammingError",
     "evalue": "1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'c.Name AS FullName,\n            c.Email AS Email,\n            c.ContactNumber AS' at line 3",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mMySQLInterfaceError\u001b[0m                       Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\mysql\\connector\\connection_cext.py:608\u001b[0m, in \u001b[0;36mCMySQLConnection.cmd_query\u001b[1;34m(self, query, raw, buffered, raw_as_string)\u001b[0m\n\u001b[0;32m    607\u001b[0m         query \u001b[38;5;241m=\u001b[39m query\u001b[38;5;241m.\u001b[39mencode(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mutf-8\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m--> 608\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_cmysql\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mquery\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    609\u001b[0m \u001b[43m        \u001b[49m\u001b[43mquery\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    610\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mraw\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    611\u001b[0m \u001b[43m        \u001b[49m\u001b[43mbuffered\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mbuffered\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    612\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw_as_string\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mraw_as_string\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    613\u001b[0m \u001b[43m        \u001b[49m\u001b[43mquery_attrs\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_query_attrs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    614\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    615\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MySQLInterfaceError \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[1;31mMySQLInterfaceError\u001b[0m: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'c.Name AS FullName,\n            c.Email AS Email,\n            c.ContactNumber AS' at line 3",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mProgrammingError\u001b[0m                          Traceback (most recent call last)",
      "Input \u001b[1;32mIn [24]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mcursor\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcustomer_join_query\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\mysql\\connector\\cursor_cext.py:330\u001b[0m, in \u001b[0;36mCMySQLCursor.execute\u001b[1;34m(self, operation, params, multi)\u001b[0m\n\u001b[0;32m    325\u001b[0m             \u001b[38;5;28;01mraise\u001b[39;00m ProgrammingError(\n\u001b[0;32m    326\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNot all parameters were used in the SQL statement\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    327\u001b[0m             )\n\u001b[0;32m    329\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 330\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_cnx\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcmd_query\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    331\u001b[0m \u001b[43m        \u001b[49m\u001b[43mstmt\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    332\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_raw\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    333\u001b[0m \u001b[43m        \u001b[49m\u001b[43mbuffered\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_buffered\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    334\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw_as_string\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_raw_as_string\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    335\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    336\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MySQLInterfaceError \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[0;32m    337\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m get_mysql_exception(\n\u001b[0;32m    338\u001b[0m         msg\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39mmsg, errno\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39merrno, sqlstate\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39msqlstate\n\u001b[0;32m    339\u001b[0m     ) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\mysql\\connector\\connection_cext.py:616\u001b[0m, in \u001b[0;36mCMySQLConnection.cmd_query\u001b[1;34m(self, query, raw, buffered, raw_as_string)\u001b[0m\n\u001b[0;32m    608\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_cmysql\u001b[38;5;241m.\u001b[39mquery(\n\u001b[0;32m    609\u001b[0m         query,\n\u001b[0;32m    610\u001b[0m         raw\u001b[38;5;241m=\u001b[39mraw,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    613\u001b[0m         query_attrs\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_query_attrs,\n\u001b[0;32m    614\u001b[0m     )\n\u001b[0;32m    615\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MySQLInterfaceError \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[1;32m--> 616\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m get_mysql_exception(\n\u001b[0;32m    617\u001b[0m         err\u001b[38;5;241m.\u001b[39merrno, msg\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39mmsg, sqlstate\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39msqlstate\n\u001b[0;32m    618\u001b[0m     ) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n\u001b[0;32m    619\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[0;32m    620\u001b[0m     addr \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m    621\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unix_socket \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unix_socket \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_host\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_port\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    622\u001b[0m     )\n",
      "\u001b[1;31mProgrammingError\u001b[0m: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'c.Name AS FullName,\n            c.Email AS Email,\n            c.ContactNumber AS' at line 3"
     ]
    }
   ],
   "source": [
    "cursor.execute(customer_join_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "24874bda",
   "metadata": {},
   "outputs": [
    {
     "ename": "ProgrammingError",
     "evalue": "1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'c.Name AS FullName,\n            c.Email AS Email,\n            c.ContactNumber AS' at line 3",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mMySQLInterfaceError\u001b[0m                       Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\mysql\\connector\\connection_cext.py:608\u001b[0m, in \u001b[0;36mCMySQLConnection.cmd_query\u001b[1;34m(self, query, raw, buffered, raw_as_string)\u001b[0m\n\u001b[0;32m    607\u001b[0m         query \u001b[38;5;241m=\u001b[39m query\u001b[38;5;241m.\u001b[39mencode(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mutf-8\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m--> 608\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_cmysql\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mquery\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    609\u001b[0m \u001b[43m        \u001b[49m\u001b[43mquery\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    610\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mraw\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    611\u001b[0m \u001b[43m        \u001b[49m\u001b[43mbuffered\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mbuffered\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    612\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw_as_string\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mraw_as_string\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    613\u001b[0m \u001b[43m        \u001b[49m\u001b[43mquery_attrs\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_query_attrs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    614\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    615\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MySQLInterfaceError \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[1;31mMySQLInterfaceError\u001b[0m: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'c.Name AS FullName,\n            c.Email AS Email,\n            c.ContactNumber AS' at line 3",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mProgrammingError\u001b[0m                          Traceback (most recent call last)",
      "Input \u001b[1;32mIn [25]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mcursor\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcustomer_join_query\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\mysql\\connector\\cursor_cext.py:330\u001b[0m, in \u001b[0;36mCMySQLCursor.execute\u001b[1;34m(self, operation, params, multi)\u001b[0m\n\u001b[0;32m    325\u001b[0m             \u001b[38;5;28;01mraise\u001b[39;00m ProgrammingError(\n\u001b[0;32m    326\u001b[0m                 \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNot all parameters were used in the SQL statement\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    327\u001b[0m             )\n\u001b[0;32m    329\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 330\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_cnx\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcmd_query\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    331\u001b[0m \u001b[43m        \u001b[49m\u001b[43mstmt\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    332\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_raw\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    333\u001b[0m \u001b[43m        \u001b[49m\u001b[43mbuffered\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_buffered\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    334\u001b[0m \u001b[43m        \u001b[49m\u001b[43mraw_as_string\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_raw_as_string\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    335\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    336\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MySQLInterfaceError \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[0;32m    337\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m get_mysql_exception(\n\u001b[0;32m    338\u001b[0m         msg\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39mmsg, errno\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39merrno, sqlstate\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39msqlstate\n\u001b[0;32m    339\u001b[0m     ) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\mysql\\connector\\connection_cext.py:616\u001b[0m, in \u001b[0;36mCMySQLConnection.cmd_query\u001b[1;34m(self, query, raw, buffered, raw_as_string)\u001b[0m\n\u001b[0;32m    608\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_cmysql\u001b[38;5;241m.\u001b[39mquery(\n\u001b[0;32m    609\u001b[0m         query,\n\u001b[0;32m    610\u001b[0m         raw\u001b[38;5;241m=\u001b[39mraw,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    613\u001b[0m         query_attrs\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_query_attrs,\n\u001b[0;32m    614\u001b[0m     )\n\u001b[0;32m    615\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m MySQLInterfaceError \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[1;32m--> 616\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m get_mysql_exception(\n\u001b[0;32m    617\u001b[0m         err\u001b[38;5;241m.\u001b[39merrno, msg\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39mmsg, sqlstate\u001b[38;5;241m=\u001b[39merr\u001b[38;5;241m.\u001b[39msqlstate\n\u001b[0;32m    618\u001b[0m     ) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n\u001b[0;32m    619\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[0;32m    620\u001b[0m     addr \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m    621\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unix_socket \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unix_socket \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_host\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_port\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    622\u001b[0m     )\n",
      "\u001b[1;31mProgrammingError\u001b[0m: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'c.Name AS FullName,\n            c.Email AS Email,\n            c.ContactNumber AS' at line 3"
     ]
    }
   ],
   "source": [
    "cursor.execute(customer_join_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acf26d88",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f'There are {len(customers)} customers with more than $60 of spending...')\n",
    "print('Printing the top 10 spenders...')\n",
    "\n",
    "for customer in customers[:10]:\n",
    "    print('=' * 50)\n",
    "    print(f'Full Name: \\t {customer[0]}')\n",
    "    print(f'Email: \\t\\t {customer[1]}')\n",
    "    print(f'Phone Number: \\t {customer[2]}')\n",
    "    print(f'Address: \\t {customer[3]}')\n",
    "    print(f'Country: \\t {customer[4]}')\n",
    "    print(f'City: \\t\\t {customer[5]}')\n",
    "    print(f'Has spent: \\t {float(custo"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
