
do $$
begin

    begin
        alter type agrego.type_report add value 'users_by_sourceEngine';
    exception when others then
        raise notice 'users_by_sourceEngine in report already exists';
    end;

end
$$;
