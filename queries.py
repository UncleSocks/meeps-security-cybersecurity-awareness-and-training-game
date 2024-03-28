

def ticket_ids(cursor):
    
    cursor.execute('SELECT id FROM tickets')
    ticket_ids_results = cursor.fetchall()
    ticket_ids_list = [ticket_ids_result[0] for ticket_ids_result in ticket_ids_results]

    return ticket_ids_list


def threats(cursor):

    cursor.execute('SELECT name FROM threats')
    threat_list_results = cursor.fetchall()
    threat_list = [threat_list_result[0] for threat_list_result in threat_list_results]

    return threat_list


def accounts(cursor):

    cursor.execute('SELECT id, name FROM accounts')
    account_list_results = cursor.fetchall()
    id_list = [account_list_result[0] for account_list_result in account_list_results]
    account_list = [account_list_result[1] for account_list_result in account_list_results]

    return id_list, account_list


def tickets(cursor):

    cursor.execute('SELECT id, title FROM tickets')
    ticket_list_results = cursor.fetchall()
    id_list = [ticket_list_result[0] for ticket_list_result in ticket_list_results]
    ticket_list = [ticket_list_result[1] for ticket_list_result in ticket_list_results]

    return id_list, ticket_list