from modelare import Node
from modelare import str_list_pairs
from modelare import generate_queue
from modelare import check_arc_consistency


if __name__ == '__main__':
    # Nodurile din exemplul incosistent
    t = Node("T", ["r", "g", "b"], [])
    v = Node("V", ["r", "g", "b"], [])
    sa = Node("SA", ["r", "g", "b"], [])
    wa = Node("WA", ["r"], [])
    nt = Node("NT", ["r", "g", "b"], [])
    q = Node("Q", ["g"], [])
    nsw = Node("NSW", ["r", "g", "b"], [])
    t.add_neighbours([v])
    v.add_neighbours([t, sa, nsw])
    sa.add_neighbours([wa, nt, nsw, q, v])
    wa.add_neighbours([nt, sa])
    nt.add_neighbours([wa, q, sa])
    q.add_neighbours([nt, sa, nsw])
    nsw.add_neighbours([q, sa, v])

    # Nodurile din exemplul consistent
    c_sa = Node("SA", ["r", "g"], [])
    c_nt = Node("NT", ["g"], [])
    c_wa = Node("WA", ["r", "g", "b"], [])
    c_sa.add_neighbours([c_nt, c_wa])
    c_nt.add_neighbours([c_wa, c_sa])
    c_wa.add_neighbours([c_nt, c_sa])

    print(str_list_pairs(generate_queue([t, v, sa, wa, nt, q, nsw])))
    print("\n")
    print(check_arc_consistency([t, v, sa, wa, nt, q, nsw]))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(str_list_pairs(generate_queue([c_nt, c_sa, c_wa])))
    print("\n")
    print(check_arc_consistency([c_nt, c_sa, c_wa]))
