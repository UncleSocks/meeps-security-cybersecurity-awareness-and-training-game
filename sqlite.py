

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
    