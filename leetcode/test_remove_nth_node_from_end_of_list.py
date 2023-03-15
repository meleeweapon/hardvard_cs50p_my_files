import remove_nth_node_from_end_of_list as r

def test_removeNthFromEnd():
  rmnthelm = r.Solution().removeNthFromEnd
  result = rmnthelm(r.list_to_linked_list([1,2,3,4,5]), 2)
  result = r.linked_list_to_list(result)
  assert result == [1,2,3,5]

  result = rmnthelm(r.list_to_linked_list([1,2]), 2)
  result = r.linked_list_to_list(result)
  assert result == [2]

  result = rmnthelm(r.list_to_linked_list([1]), 1)
  result = r.linked_list_to_list(result)
  assert result == []