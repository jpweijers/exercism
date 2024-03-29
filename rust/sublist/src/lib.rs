#[derive(Debug, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    if _first_list == _second_list {
        return Comparison::Equal
    }
    if _first_list.len() < _second_list.len() {
        return Comparison::Sublist
    }
    if _first_list.len() > _second_list.len() {
        return Comparison::Superlist
    }
    Comparison::Unequal
}
