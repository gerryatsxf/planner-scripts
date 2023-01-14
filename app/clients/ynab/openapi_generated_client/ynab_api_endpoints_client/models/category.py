import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.category_goal_type import CategoryGoalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Category")


@attr.s(auto_attribs=True)
class Category:
    """
    Attributes:
        id (str):
        category_group_id (str):
        name (str):
        hidden (bool): Whether or not the category is hidden
        budgeted (int): Budgeted amount in milliunits format
        activity (int): Activity amount in milliunits format
        balance (int): Balance in milliunits format
        deleted (bool): Whether or not the category has been deleted.  Deleted categories will only be included in delta
            requests.
        original_category_group_id (Union[Unset, str]): If category is hidden this is the id of the category group it
            originally belonged to before it was hidden.
        note (Union[Unset, str]):
        goal_type (Union[Unset, None, CategoryGoalType]): The type of goal, if the category has a goal (TB='Target
            Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')
        goal_creation_month (Union[Unset, datetime.date]): The month a goal was created
        goal_target (Union[Unset, int]): The goal target amount in milliunits
        goal_target_month (Union[Unset, datetime.date]): The original target month for the goal to be completed.  Only
            some goal types specify this date.
        goal_percentage_complete (Union[Unset, int]): The percentage completion of the goal
        goal_months_to_budget (Union[Unset, int]): The number of months, including the current month, left in the
            current goal period.
        goal_under_funded (Union[Unset, int]): The amount of funding still needed in the current month to stay on track
            towards completing the goal within the current goal period.  This amount will generally correspond to the
            'Underfunded' amount in the web and mobile clients except when viewing a category with a Needed for Spending
            Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when
            viewing category with a Needed for Spending Goal in a future month.
        goal_overall_funded (Union[Unset, int]): The total amount funded towards the goal within the current goal
            period.
        goal_overall_left (Union[Unset, int]): The amount of funding still needed to complete the goal within the
            current goal period.
    """

    id: str
    category_group_id: str
    name: str
    hidden: bool
    budgeted: int
    activity: int
    balance: int
    deleted: bool
    original_category_group_id: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    goal_type: Union[Unset, None, CategoryGoalType] = UNSET
    goal_creation_month: Union[Unset, datetime.date] = UNSET
    goal_target: Union[Unset, int] = UNSET
    goal_target_month: Union[Unset, datetime.date] = UNSET
    goal_percentage_complete: Union[Unset, int] = UNSET
    goal_months_to_budget: Union[Unset, int] = UNSET
    goal_under_funded: Union[Unset, int] = UNSET
    goal_overall_funded: Union[Unset, int] = UNSET
    goal_overall_left: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        category_group_id = self.category_group_id
        name = self.name
        hidden = self.hidden
        budgeted = self.budgeted
        activity = self.activity
        balance = self.balance
        deleted = self.deleted
        original_category_group_id = self.original_category_group_id
        note = self.note
        goal_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.goal_type, Unset):
            goal_type = self.goal_type.value if self.goal_type else None

        goal_creation_month: Union[Unset, str] = UNSET
        if not isinstance(self.goal_creation_month, Unset):
            goal_creation_month = self.goal_creation_month.isoformat()

        goal_target = self.goal_target
        goal_target_month: Union[Unset, str] = UNSET
        if not isinstance(self.goal_target_month, Unset):
            goal_target_month = self.goal_target_month.isoformat()

        goal_percentage_complete = self.goal_percentage_complete
        goal_months_to_budget = self.goal_months_to_budget
        goal_under_funded = self.goal_under_funded
        goal_overall_funded = self.goal_overall_funded
        goal_overall_left = self.goal_overall_left

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category_group_id": category_group_id,
                "name": name,
                "hidden": hidden,
                "budgeted": budgeted,
                "activity": activity,
                "balance": balance,
                "deleted": deleted,
            }
        )
        if original_category_group_id is not UNSET:
            field_dict["original_category_group_id"] = original_category_group_id
        if note is not UNSET:
            field_dict["note"] = note
        if goal_type is not UNSET:
            field_dict["goal_type"] = goal_type
        if goal_creation_month is not UNSET:
            field_dict["goal_creation_month"] = goal_creation_month
        if goal_target is not UNSET:
            field_dict["goal_target"] = goal_target
        if goal_target_month is not UNSET:
            field_dict["goal_target_month"] = goal_target_month
        if goal_percentage_complete is not UNSET:
            field_dict["goal_percentage_complete"] = goal_percentage_complete
        if goal_months_to_budget is not UNSET:
            field_dict["goal_months_to_budget"] = goal_months_to_budget
        if goal_under_funded is not UNSET:
            field_dict["goal_under_funded"] = goal_under_funded
        if goal_overall_funded is not UNSET:
            field_dict["goal_overall_funded"] = goal_overall_funded
        if goal_overall_left is not UNSET:
            field_dict["goal_overall_left"] = goal_overall_left

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        category_group_id = d.pop("category_group_id")

        name = d.pop("name")

        hidden = d.pop("hidden")

        budgeted = d.pop("budgeted")

        activity = d.pop("activity")

        balance = d.pop("balance")

        deleted = d.pop("deleted")

        original_category_group_id = d.pop("original_category_group_id", UNSET)

        note = d.pop("note", UNSET)

        _goal_type = d.pop("goal_type", UNSET)
        goal_type: Union[Unset, None, CategoryGoalType]
        if _goal_type is None:
            goal_type = None
        elif isinstance(_goal_type, Unset):
            goal_type = UNSET
        else:
            goal_type = CategoryGoalType(_goal_type)

        _goal_creation_month = d.pop("goal_creation_month", UNSET)
        goal_creation_month: Union[Unset, datetime.date]
        if isinstance(_goal_creation_month, Unset):
            goal_creation_month = UNSET
        else:
            goal_creation_month = isoparse(_goal_creation_month).date()

        goal_target = d.pop("goal_target", UNSET)

        _goal_target_month = d.pop("goal_target_month", UNSET)
        goal_target_month: Union[Unset, datetime.date]
        if isinstance(_goal_target_month, Unset):
            goal_target_month = UNSET
        else:
            goal_target_month = isoparse(_goal_target_month).date()

        goal_percentage_complete = d.pop("goal_percentage_complete", UNSET)

        goal_months_to_budget = d.pop("goal_months_to_budget", UNSET)

        goal_under_funded = d.pop("goal_under_funded", UNSET)

        goal_overall_funded = d.pop("goal_overall_funded", UNSET)

        goal_overall_left = d.pop("goal_overall_left", UNSET)

        category = cls(
            id=id,
            category_group_id=category_group_id,
            name=name,
            hidden=hidden,
            budgeted=budgeted,
            activity=activity,
            balance=balance,
            deleted=deleted,
            original_category_group_id=original_category_group_id,
            note=note,
            goal_type=goal_type,
            goal_creation_month=goal_creation_month,
            goal_target=goal_target,
            goal_target_month=goal_target_month,
            goal_percentage_complete=goal_percentage_complete,
            goal_months_to_budget=goal_months_to_budget,
            goal_under_funded=goal_under_funded,
            goal_overall_funded=goal_overall_funded,
            goal_overall_left=goal_overall_left,
        )

        category.additional_properties = d
        return category

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
