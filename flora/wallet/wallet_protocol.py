from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Set

from blspy import G1Element
from typing_extensions import Protocol

from flora.server.ws_connection import WSFloraConnection
from flora.types.blockchain_format.coin import Coin
from flora.types.blockchain_format.sized_bytes import bytes32
from flora.util.ints import uint32, uint64, uint128
from flora.wallet.util.wallet_types import WalletType
from flora.wallet.wallet_coin_record import WalletCoinRecord
from flora.wallet.wallet_info import WalletInfo

if TYPE_CHECKING:
    from flora.wallet.wallet_state_manager import WalletStateManager


class WalletProtocol(Protocol):
    @classmethod
    def type(cls) -> WalletType:
        ...

    def id(self) -> uint32:
        ...

    async def coin_added(self, coin: Coin, height: uint32, peer: WSFloraConnection) -> None:
        ...

    async def select_coins(
        self,
        amount: uint64,
        exclude: Optional[List[Coin]] = None,
        min_coin_amount: Optional[uint64] = None,
        max_coin_amount: Optional[uint64] = None,
        excluded_coin_amounts: Optional[List[uint64]] = None,
    ) -> Set[Coin]:
        ...

    async def get_confirmed_balance(self, record_list: Optional[Set[WalletCoinRecord]] = None) -> uint128:
        ...

    async def get_unconfirmed_balance(self, unspent_records: Optional[Set[WalletCoinRecord]] = None) -> uint128:
        ...

    async def get_spendable_balance(self, unspent_records: Optional[Set[WalletCoinRecord]] = None) -> uint128:
        ...

    async def get_pending_change_balance(self) -> uint64:
        ...

    async def get_max_send_amount(self, records: Optional[Set[WalletCoinRecord]] = None) -> uint128:
        ...

    # not all wallet supports this. To signal support, make
    # require_derivation_paths() return true
    def puzzle_hash_for_pk(self, pubkey: G1Element) -> bytes32:
        ...

    def require_derivation_paths(self) -> bool:
        ...

    def get_name(self) -> str:
        ...

    wallet_info: WalletInfo
    # WalletStateManager is only imported for type hinting thus leaving pylint
    # unable to process this
    wallet_state_manager: WalletStateManager  # pylint: disable=used-before-assignment
