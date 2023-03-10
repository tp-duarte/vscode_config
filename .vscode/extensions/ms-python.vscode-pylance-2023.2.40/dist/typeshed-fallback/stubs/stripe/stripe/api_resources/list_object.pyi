from _typeshed import Incomplete
from collections.abc import Iterator
from typing import Any

from stripe import api_requestor as api_requestor
from stripe.stripe_object import StripeObject as StripeObject

class ListObject(StripeObject):
    OBJECT_NAME: str
    def list(
        self,
        api_key: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ) -> ListObject: ...
    def create(
        self,
        api_key: Incomplete | None = ...,
        idempotency_key: str | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ): ...
    def retrieve(
        self,
        id,
        api_key: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ): ...
    def __getitem__(self, k): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __reversed__(self): ...
    def auto_paging_iter(self) -> Iterator[Any]: ...
    @classmethod
    def empty_list(
        cls, api_key: Incomplete | None = ..., stripe_version: Incomplete | None = ..., stripe_account: Incomplete | None = ...
    ) -> ListObject: ...
    @property
    def is_empty(self) -> bool: ...
    def next_page(
        self,
        api_key: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ) -> ListObject: ...
    def previous_page(
        self,
        api_key: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        **params,
    ) -> ListObject: ...
