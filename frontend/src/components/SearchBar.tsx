type Props = {
  search: string;
  setSearch: (value: string) => void;
};

function SearchBar({ search, setSearch }: Props) {
  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search supplier, asset, owner..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </div>
  );
}

export default SearchBar;